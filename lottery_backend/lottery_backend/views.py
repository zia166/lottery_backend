from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
from .sample_data import data
import random
from .serializers import PerformanceSerializer, WinnerSerializer, LotteryEntrySerializer
from .models import Performance, LotteryEntry, Winner
from django.db.models import Max
from django.db.models import Avg

class PerformanceViewSet(viewsets.ViewSet):
    def list(self, request):
        performances = Performance.objects.all()
        serializer = PerformanceSerializer(performances, many=True)
        return Response(serializer.data)

class WinnerViewSet(viewsets.ViewSet):
        def list(self, request):
            winners = Winner.objects.all()
            winners_data = []
            performances_data = []
            for winner in winners:
                performance = Performance.objects.get(performance_id=winner.performance_id)
                winner_data = {
                    'performance': winner.performance,
                    'performance_name': performance,
                    'username': winner.username,
                    'no_of_ticket': winner.no_of_ticket,
                    'winning_time': winner.winning_time,
                }
                winners_data.append(winner_data)
                performance_data = {
                    'performance_name': performance.performance_name
                }
                performances_data.append(performance_data)
                
           
            serializer = WinnerSerializer(winners_data, many=True)
            serialized_data = serializer.data
            response_data = {
                'winners': serialized_data,
                'performances': performances_data
            }

            return Response(response_data)
     
        def create(self, request):
            performances = Performance.objects.all()
            total_available_tickets = performances.aggregate(average_tickets=Avg('available_tickets'))['average_tickets']
            print(total_available_tickets)
            
            winners = []
            for performance in performances:
                if performance.available_tickets >= total_available_tickets:
                    print(performance.available_tickets)
                    entries = LotteryEntry.objects.filter(performance=performance).order_by('entry_time')
                    winners.extend(entries)
            print("winners",winners)
            if winners:
                random_winner = random.choice(winners)
                print(random_winner)
            #   Check if the winners table is initially empty
            if not Winner.objects.exists():
                # Create a new Winner object and save it to the database
                winner = Winner.objects.create(
                    performance_id=random_winner.performance.performance_id,
                    username=random_winner.username,
                    no_of_ticket=random_winner.no_of_tickets,
                    winning_time=random_winner.entry_time
                )
                winner.save()
            else:
                return Response({'message': 'Winners already selected'})
                
            return Response({'message': 'Winners selected successfully'})
  

class LotteryEntryViewSet(viewsets.ModelViewSet):
    queryset = LotteryEntry.objects.all()
    serializer_class = LotteryEntrySerializer
    def list(self, request):
        entries = LotteryEntry.objects.all()
        serializer = LotteryEntrySerializer(entries, many=True)
        return Response(serializer.data)
    def destroy(self, request):
        print(request.data)
        entry = LotteryEntry.objects.get()
        entry.delete()
        return Response(status=204)
    def create(self, request, *args, **kwargs):
        data = request.data
        tickets = data.get('Tickets')
        show_name = data.get('ShowName')
        date_str = data.get('ShowDate')
        time_str= data.get('ShowTime')
        user_name = data.get('UserName')
        time_obj = datetime.strptime(time_str, '%I:%M %p')
        show_time = time_obj.strftime('%H:%M:%S')
        # Retrieve the Performance instance using the show_name
        try:
            performance = Performance.objects.get(performance_name=show_name)
            print(performance)
            performance_id = performance.pk
        except Performance.DoesNotExist:
            raise ValueError('Performance with the provided name does not exist')
        
        # Create the LotteryEntry instance with the retrieved Performance instance
        lottery_entry = LotteryEntry.objects.create(
            username=user_name,
            performance_name=performance,
            no_of_tickets=tickets,
            show_time=show_time,
            entry_time=datetime.utcnow().isoformat(),
            performance_id=performance_id
        )

        return Response({'message': 'Created successfully'})