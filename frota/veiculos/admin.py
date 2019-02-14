from django.contrib import admin
from django.utils.html import format_html
from .models import departamento,responsavel,veiculo,combustivel,posto,tabelacombustivel,manutencao, empresa, requisicao
# Register your models here.

class departamentoAdmin(admin.ModelAdmin):
    pass


class responsavelAdmin(admin.ModelAdmin):
    pass

class veiculoAdmin(admin.ModelAdmin):
    pass

class combustivelAdmin(admin.ModelAdmin):
    pass

class postoAdmin(admin.ModelAdmin):
    pass

class tabelacombustivelAdmin(admin.ModelAdmin):
    pass

class manutencaoAdmin(admin.ModelAdmin):
    pass

class empresaAdmin(admin.ModelAdmin):
    pass

class requisicaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(departamento, departamentoAdmin)
admin.site.register(responsavel, responsavelAdmin)
admin.site.register(veiculo, veiculoAdmin)
admin.site.register(combustivel, combustivelAdmin)
admin.site.register(posto, postoAdmin)
admin.site.register(tabelacombustivel,tabelacombustivelAdmin)
admin.site.register(manutencao, manutencaoAdmin)
admin.site.register(empresa, empresaAdmin)
admin.site.register(requisicao, requisicaoAdmin)
