from board.views import EventReportView, SeminarListView, MakePostView, \
    PlayStormingListView, SeminarDetailView, PlayStormingDetailView, AnnouncementListView, GraduatingBoardListView, \
    StudentBoardListView, AnnouncementDetailView, GraduatingBoardDetailView, StudentBoardDetailView, SeminarDeleteView, \
    PlayStormingDeleteView, AnnouncementDeleteView, StudentBoardDeleteView, GraduatingBoardDeleteView, EditPostView
from django.conf.urls import url

urlpatterns = [
    url(r'^playstorming$', PlayStormingListView.as_view(), name='playstorming'),
    url(r'^seminar$', SeminarListView.as_view(), name='seminar'),
    url(r'^seminar/(?P<id>\d+)/?$', SeminarDetailView.as_view(), name='seminar_detail'),
    url(r'^seminar/delete/(?P<id>\d+)/?$', SeminarDeleteView.as_view(), name='seminar_delete'),
    url(r'^playstorming/(?P<id>\d+)/?$', PlayStormingDetailView.as_view(), name='playstorming_detail'),
    url(r'^playstorming/delete/(?P<id>\d+)/?$', PlayStormingDeleteView.as_view(), name='playstorming_delete'),
    url(r'^event_report$', EventReportView.as_view(), name='event_report'),
    url(r'^write_post$', MakePostView.as_view(), name='write_post'),
    url(r'^edit_post$', EditPostView.as_view(), name='edit_post'),
    url(r'^announcement$', AnnouncementListView.as_view(), name='announcement'),
    url(r'^announcement/(?P<id>\d+)/?$', AnnouncementDetailView.as_view(), name='announcement_detail'),
    url(r'^announcement/delete/(?P<id>\d+)/?$', AnnouncementDeleteView.as_view(), name='announcement_delete'),
    url(r'^graduating$', GraduatingBoardListView.as_view(), name='graduating'),
    url(r'^graduating/(?P<id>\d+)/?$', GraduatingBoardDetailView.as_view(), name='graduating_detail'),
    url(r'^graduating/delete/(?P<id>\d+)/?$', GraduatingBoardDeleteView.as_view(), name='graduating_delete'),
    url(r'^student$', StudentBoardListView.as_view(), name='student'),
    url(r'^student/(?P<id>\d+)/?$', StudentBoardDetailView.as_view(), name='student_detail'),
    url(r'^student/delete/(?P<id>\d+)/?$', StudentBoardDeleteView.as_view(), name='student_delete')
]