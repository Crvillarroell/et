def total_carrito(request):
    total = 0
    if request.user in request.session:
        try:
            for key,value in request.session['carro'].items():
                total = total + (int(value['precio']))*(value['cantidad'])
        except:
            request.session['carro'] = {}
            total = 0
    return{'total_carro':int(total)}