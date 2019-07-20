from django.shortcuts import render
from django.views import generic


# Create your views here.
from resumeappc.models import Education, Experience, JobHistory, PersonalInfo, SkillsSummary
def index(request):

    # Generate counts of some of the main objects
    num_Education = Education.objects.all().count()
    num_Experience = Experience.objects.all().count()
    num_JobHistory =    JobHistory.objects.all().count()
    num_SkillsSummary = SkillsSummary.objects.all().count()
           
    # The 'all()' is implied by default.    
    num_PersonalInfo = PersonalInfo.objects.count()
    
    context = {
        'num_Education': num_Education,
        'num_Experience': num_Experience,
        'num_PersonalInfo': num_PersonalInfo,
        'num_JobHistory': num_JobHistory,
        'num_SkillsSummary': num_SkillsSummary,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
class EducationListView(generic.ListView):
    model = Education
class EducationDetailView(generic.DetailView):
    model = Education
