/* global settings */
import 'core-js/actual'
import 'bootstrap/js/dist/collapse'

import DatasetsList from './components/datasets-list'
import DatasetFilter from './components/dataset-filter' // Using the combined component
import DatasetDisplay from './components/dataset-display'
import { queryAllByComponent } from './util' // Note: Using a "queryAll" variant

const urlSearchParams = new URLSearchParams(window.location.search)
const params = Object.fromEntries(urlSearchParams.entries())

// 1. Native replacement for $.getJSON using the Fetch API
let datasetsCache = null
async function getDatasets () {
  if (!datasetsCache) {
    const response = await fetch(`${settings.BASE_URL}/datasets.json`)
    datasetsCache = await response.json()
  }
  return datasetsCache
}

// 2. Updated component list (pointing both filters to DatasetFilter)
const components = [
  { tag: 'dataset-display', class: DatasetDisplay },
  { tag: 'datasets-list', class: DatasetsList, usesDatasets: true },
  { tag: 'categories-filter', class: DatasetFilter, type: 'category', usesDatasets: true },
  { tag: 'organizations-filter', class: DatasetFilter, type: 'organization', usesDatasets: true }
]

// 3. Native initialization loop
async function init () {
  for (const component of components) {
    // Look for all instances of the component on the page
    const els = queryAllByComponent(component.tag)
    
    if (els.length > 0) {
      if (component.usesDatasets) {
        const datasets = await getDatasets()
        els.forEach(el => {
          new component.class({ el, params, datasets, type: component.type })
        })
      } else {
        els.forEach(el => {
          new component.class({ el, params })
        })
      }
    }
  }
}

init()
