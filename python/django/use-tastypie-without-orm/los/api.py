from los.lo import LO, DATA
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import Resource, Bundle


class LOResource(Resource):
    pk = fields.IntegerField(attribute='pk')
    title = fields.CharField(attribute='title', default="")
    description = fields.CharField(attribute='description', default="")

    class Meta:
        resource_name = 'lo'
        object_class = LO
        authorization = Authorization()
        offset = 100
        limit = 100

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}
#        print bundle_or_obj.request.META['HTTP_HOST']
        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.pk
        else:
            if bundle_or_obj is not None:
                kwargs['pk'] = bundle_or_obj.pk
        kwargs['resource_name'] = self._meta.resource_name
        if self._meta.api_name is not None:
            kwargs['api_name'] = self._meta.api_name

        return kwargs

    def get_object_list(self, request):
        return DATA

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)

    def obj_get(self, bundle, **kwargs):
        all_obj = DATA
        obj = filter(lambda x: int(x.pk) == int(kwargs['pk']), all_obj)
        if obj != []:
            return obj[0]
