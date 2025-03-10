from rubicon.objc import Block, NSMakeRect, NSSize, objc_id

from toga_iOS.libs import (
    UIGraphicsImageRenderer,
    UIGraphicsImageRendererContext,
    UIImage,
)


class Icon:
    EXTENSIONS = [".icns", ".png", ".bmp", ".ico"]
    SIZES = None

    def __init__(self, interface, path):
        self.interface = interface

        if path is None:
            self.native = None
            raise FileNotFoundError("No runtime app icon")

        self.path = path
        self.native = UIImage.imageWithContentsOfFile(str(path))
        if self.native is None:
            raise ValueError(f"Unable to load icon from {path}")

    def _as_size(self, size):
        renderer = UIGraphicsImageRenderer.alloc().initWithSize(NSSize(size, size))

        def _resize(context: UIGraphicsImageRendererContext) -> None:
            self.native.drawInRect(NSMakeRect(0, 0, size, size))

        return renderer.imageWithActions(Block(_resize, None, objc_id))
