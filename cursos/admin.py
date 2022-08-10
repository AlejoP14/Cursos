
from typing import Optional, Sequence
from django.contrib import admin
from .models import ComentarioContacto, Cursos
from .models import Actividad
from .models import Comentario

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

class AdministartModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('NombreCurso', 'Descripcion')

    
    
admin.site.register(Cursos, AdministartModelo)


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id','descripCurso')
    search_fields: Sequence[str] = ('id','created')
    date_hierarchy = 'created'
    readonly_fields: Sequence[str] = ('created', 'id')
    
admin.site.register(Actividad, AdministrarComentarios)

class AdministrarMdelo(admin.ModelAdmin):
    readonly_fields = ('create','update')
    list_display = ('id','titulo', 'descripcion',)
    search_fields = ('titulo','descripcion')
    date_hierarchy = 'create'
    list_filter = ('id','titulo')

    list_per_page=2 
    list_display_links=('descripcion',)
    list_editable=('titulo',)