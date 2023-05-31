def crud(routes: [type]) -> set:
    fonctions = set()

    for route in routes:
        router = route()
        fonctions.update(
            getattr(router, attr)
            for attr in dir(router)
            if not attr.startswith("__") and callable(getattr(router, attr))
        )

    return fonctions
