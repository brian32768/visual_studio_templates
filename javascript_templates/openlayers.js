// Inspired by the book "OpenLayers 3.x Cookbook Second Edition"

// This has to be run via parcel
// which uses node to translate these imports to something usable in a browser

import './node_modules/ol/ol.css';
import { Map, View } from "./node_modules/ol";
import TileLayer from "./node_modules/ol/layer/Tile";
import OSM  from "./node_modules/ol/source/OSM";

var map = new Map({
    target: 'map',
    layers: [
        new TileLayer({
            source: new OSM()
        })
    ],
    view: new View({
        center: [-13760000, 5800000],
        zoom: 10
    })
});

// Hot Module Replacement
if (module.hot) {
    module.hot.accept()
}

console.log('Project js loaded');
