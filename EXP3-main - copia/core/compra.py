class Carro:
    def _init_ (self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro=carro
    
    def agregar(self, crear):
        if crear.codigo not in self.carro.keys():
            self.carrito[crear.codigo]={
                "codigo": crear.codigo,
                "nombre": crear.nombre,
                "precio": str(crear.precio) ,
                "stock": crear.stock,
                "cantidad" : 1,
                "total": crear.precio,
                
            }