from django.shortcuts import render  # type: ignore[reportMissingImports]


def inicio(request):
    return render(
        request,
        'inicio.html'
    )
