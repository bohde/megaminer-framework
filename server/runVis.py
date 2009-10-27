#!/usr/bin/env python

from visualizer.visualizer import FileVisualizer

if __name__ == "__main__":
    vis = FileVisualizer("visualizer/test/1.gamelog", {"width":1280, "height":800})
    vis.mainloop()
