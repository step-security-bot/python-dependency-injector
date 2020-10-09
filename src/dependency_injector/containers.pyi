from types import ModuleType
from typing import Type, Dict, Tuple, Optional, Any, Union, ClassVar, Callable as _Callable, Iterable

from .providers import Provider


class Container:
    provider_type: Type[Provider] = Provider
    providers: Dict[str, Provider]
    overridden: Tuple[Provider]
    def __init__(self) -> None: ...
    def __deepcopy__(self, memo: Optional[Dict[str, Any]]) -> Provider: ...
    def __setattr__(self, name: str, value: Union[Provider, Any]) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def set_providers(self, **providers: Provider): ...
    def override(self, overriding: DynamicContainer) -> None: ...
    def override_providers(self, **overriding_providers: Provider) -> None: ...
    def reset_last_overriding(self) -> None: ...
    def reset_override(self) -> None: ...
    def resolve_provider_name(self, provider_to_resolve: Provider) -> Optional[str]: ...
    def wire(self, modules: Optional[Iterable[ModuleType]] = None, packages: Optional[Iterable[ModuleType]] = None) -> None: ...
    def unwire(self) -> None: ...


class DynamicContainer(Container): ...


class DeclarativeContainer(Container):
    cls_providers: ClassVar[Dict[str, Provider]]
    inherited_providers: ClassVar[Dict[str, Provider]]
    def __init__(self, **overriding_providers: Union[Provider, Any]) -> None: ...


def override(container: Container) -> _Callable[[Container], Container]: ...


def copy(container: Container) -> _Callable[[Container], Container]: ...

def is_container(instance: Any) -> bool: ...