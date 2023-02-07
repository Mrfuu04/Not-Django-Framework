from that_app.views import index_view, about_view, IndexView

urls = {
    '': index_view,
    '/about': about_view,
    '/my_form': IndexView,
}
