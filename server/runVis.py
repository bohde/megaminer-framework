#!/usr/bin/env python

from visualizer.visualizer import FileVisualizer

if __name__ == "__main__":
    vis = FileVisualizer("visualizer/test/0.gamelog")
    vis.mainloop()
