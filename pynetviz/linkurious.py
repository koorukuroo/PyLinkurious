# -*- coding: utf8 -*-
import random
from string import Template
from IPython.display import display, HTML
import networkx as nx

'''
    PyNetViz(Python Network Vizualization for linkurious) as nvl

    File name: linkurious.py
    Author: Kyunghoon Kim
    Date created: 10/06/2015
    Date last modified: 10/06/2015
    Python Version: 2.7
'''
__author__ = "Kyunghoon Kim"
__version__ = "0.1.0"
__email__ = "kyunghoon@unist.ac.kr"

def node_info(G, node_name, alpha=0.6, r=0, g=0, b=204, x=0, y=0, size=1):
    """Allocate a attribute of each node.
    
    Parameters
    ----------
    G: networkx.classes.graph.Graph
        Graph
    node_name: string or int
        Node Label
    alpha: float
        Transparent
    r: int
        Red of RGB
    g: int
        Green of RGB
    b: int
        Blue of RGB
    x: float
        position of x-axis
    y: float
        position of y-axis
    size: float
        size of node
    """
    if x == 0:
        x = random.random()
    if y == 0:
        y = random.random()
    G.node[node_name]['label'] = node_name
    G.node[node_name]['viz'] = {'color': {'a': alpha, 'r': r, 'g': g, 'b': b},
        'position': {'x': x, 'y': y, 'z': 0.0},
        'size': size}
    return G

def make_html(drawEdges, gexfname='./NetworkX_Graph.gexf', filename='./NetworkX_Graph.html'):
    html = """
<!-- START SIGMA IMPORTS -->
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/sigma.core.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/conrad.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/utils/sigma.utils.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/utils/sigma.polyfills.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/sigma.settings.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/classes/sigma.classes.dispatcher.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/classes/sigma.classes.configurable.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/classes/sigma.classes.graph.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/classes/sigma.classes.camera.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/classes/sigma.classes.quad.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/captors/sigma.captors.mouse.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/captors/sigma.captors.touch.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/sigma.renderers.canvas.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/sigma.renderers.webgl.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/sigma.renderers.svg.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/sigma.renderers.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/webgl/sigma.webgl.nodes.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/webgl/sigma.webgl.nodes.fast.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/webgl/sigma.webgl.edges.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/webgl/sigma.webgl.edges.fast.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/webgl/sigma.webgl.edges.arrow.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.labels.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.hovers.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.nodes.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.edges.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.edges.curve.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.edges.arrow.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.edges.curvedArrow.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.edgehovers.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.edgehovers.curve.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.edgehovers.arrow.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.edgehovers.curvedArrow.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/canvas/sigma.canvas.extremities.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/svg/sigma.svg.utils.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/svg/sigma.svg.nodes.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/svg/sigma.svg.edges.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/svg/sigma.svg.edges.curve.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/svg/sigma.svg.labels.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/renderers/svg/sigma.svg.hovers.def.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/middlewares/sigma.middlewares.rescale.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/middlewares/sigma.middlewares.copy.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/misc/sigma.misc.animation.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/misc/sigma.misc.bindEvents.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/misc/sigma.misc.bindDOMEvents.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/src/misc/sigma.misc.drawHovers.js"></script>
<!-- END SIGMA IMPORTS -->
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/plugins/sigma.parsers.gexf/gexf-parser.js"></script>
<script src="https://cdn.rawgit.com/Linkurious/linkurious.js/develop/plugins/sigma.parsers.gexf/sigma.parsers.gexf.js"></script>
<div id="container">
  <style>
    #graph-container {
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      position: absolute;
    }
  </style>
  <div id="graph-container"></div>
</div>
<script>
/**
 * Here is just a basic example on how to properly display a graph
 * exported from Gephi in the GEXF format.
 *
 * The plugin sigma.parsers.gexf can load and parse the GEXF graph file,
 * and instantiate sigma when the graph is received.
 *
 * The object given as the second parameter is the base of the instance
 * configuration object. The plugin will just add the "graph" key to it
 * before the instanciation.
 */
sigma.parsers.gexf('$gexfname', {
  container: 'graph-container',
  settings: {
    drawEdges: $drawEdges
  }
}, 1);
</script>
    """
    s = Template(html).safe_substitute(drawEdges = drawEdges, gexfname = gexfname)
    HTMLfile = open(filename, 'w')
    HTMLfile.write(s)
    HTMLfile.close()

def make_gexf(G, layout=None, size=None, filename='./NetworkX_Graph.gexf'):
    if layout and size:
        for node in G.nodes():
            G = node_info(G, node, size=size[node], x=layout[node][0], y=layout[node][1])
    elif layout and not size:
        for node in G.nodes():
            G = node_info(G, node, x=layout[node][0], y=layout[node][1])
    elif not layout and size:
        for node in G.nodes():
            G = node_info(G, node, size=size[node])
    else:
        for node in G.nodes():
            G = node_info(G, node)
    nx.write_gexf(G, filename)

def view_html(filename='./NetworkX_Graph.html', height=500):
    """Display the html file.
    
    Parameters
    ----------
    filename: string
        location of html file
    height: int
        height of iframe
    """
    html = """<iframe name="pylinkurious-iframe"
    src="$filename"
    width="100%"
    height="$height"
    frameborder="0"
    webkitallowfullscreen mozallowfullscreen allowfullscreen>
    </iframe>"""
    s = Template(html).safe_substitute(filename = filename, height = height)
    display(HTML(s))

