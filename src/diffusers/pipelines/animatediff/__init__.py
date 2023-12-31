from typing import TYPE_CHECKING

from ...utils import (
    DIFFUSERS_SLOW_IMPORT,
    OptionalDependencyNotAvailable,
    _LazyModule,
    get_objects_from_module,
    is_torch_available,
    is_transformers_available,
)


_dummy_objects = {}
_import_structure = {}

try:
    if not (is_transformers_available() and is_torch_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ...utils import dummy_torch_and_transformers_objects

    _dummy_objects.update(get_objects_from_module(dummy_torch_and_transformers_objects))
else:
    _import_structure["pipeline_animatediff"] = ["AnimateDiffPipeline", "AnimateDiffPipelineOutput"]
    _import_structure["pipeline_animatediff_img2video"] = [
        "AnimateDiffImg2VideoPipeline",
        "AnimateDiffImg2VideoPipelineOutput",
    ]
    _import_structure["pipeline_animatediff_video2video"] = [
        "AnimateDiffVideo2VideoPipeline",
        "AnimateDiffVideo2VideoPipelineOutput",
    ]

if TYPE_CHECKING or DIFFUSERS_SLOW_IMPORT:
    try:
        if not (is_transformers_available() and is_torch_available()):
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        from ...utils.dummy_torch_and_transformers_objects import *

    else:
        from .pipeline_animatediff import AnimateDiffPipeline, AnimateDiffPipelineOutput
        from .pipeline_animatediff_img2video import AnimateDiffImg2VideoPipeline, AnimateDiffImg2VideoPipelineOutput
        from .pipeline_animatediff_video2video import (
            AnimateDiffVideo2VideoPipeline,
            AnimateDiffVideo2VideoPipelineOutput,
        )

else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )
    for name, value in _dummy_objects.items():
        setattr(sys.modules[__name__], name, value)
