import uuid


def get_visitor_id(request):
    #visitor_id =  None 
    if not request.session.get('visitor_id'):
        request.session['visitor_id'] =  visitor_id  = str(uuid.uuid4())
        #visitor_id  = request.session.get('visitor_id', )
        #request.session.modified = True
        return visitor_id
    else:
        visitor_id = request.session.get('visitor_id')
        return visitor_id