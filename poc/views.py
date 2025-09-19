from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Task # Certifique-se de que a importação do seu modelo está correta
from django.views.decorators.csrf import csrf_exempt # Para desativar o CSRF em um POST simplificado

@csrf_exempt
def task_list(request):
    # Lógica de POST: Adiciona uma nova tarefa
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')

    # Lógica de GET: Gera a página para exibir as tarefas
    
    # 1. Construir a string HTML do formulário
    content = """
    <h1>Minhas Tarefas</h1>
    <form method='post'>
      <input type='text' name='title' placeholder='Adicione uma nova tarefa' required>
      <button type='submit'>Adicionar</button>
    </form>
    <hr>
    """
    
    # 2. Iterar sobre as tarefas e adicionar à string
    tasks = Task.objects.all().order_by('-created')
    
    if not tasks:
        content += "Nenhuma tarefa encontrada."
    else:
        content += "<ul>"
        for task in tasks:
            # Substitua 'title' pelo nome real do campo no seu modelo Task, se for diferente
            content += f"<li>{task.title}</li>"
        content += "</ul>"
        
    # 3. Retornar a string como um HttpResponse
    return HttpResponse(content)