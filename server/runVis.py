#!/usr/bin/env python

from visualizer.visualizer import FileVisualizer
import signal, sys

if __name__ == "__main__":
    try:
        vis = FileVisualizer("visualizer/test/4.gamelog", {"width":1280, "height":800})
        vis.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)
