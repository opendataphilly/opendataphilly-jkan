/**
 * Usage:
 * <div data-component="datasets-list">
 *   <div class="datasets-count" data-hook="datasets-count"></div>
 *   <input type="text" data-hook="search-query" placeholder="Search..." class="form-control">
 *   <div data-hook="datasets-items"></div>
 * </div>
 *
 * Optionally, add filters to the component element such as
 *   data-organization="sample-department"
 *   data-category="education"
 */
import {pick, defaults, filter, debounce} from 'lodash'
import Fuse from 'fuse.js'

import TmplDatasetItem from '../templates/dataset-item'
import {queryByHook, setContent, createDatasetFilters} from '../util'

const EMPTY_STATE_HTML = '<p class="text-muted mt-3">No datasets match your search. Try a broader term or browse by tag.</p>'

function countLabel (n) {
  return n + ' dataset' + (n === 1 ? '' : 's')
}

export default class {
  constructor (opts) {
    const elements = {
      datasetsItems: queryByHook('datasets-items', opts.el),
      datasetsCount: queryByHook('datasets-count', opts.el),
      searchQuery: queryByHook('search-query', opts.el)
    }

    // Filter datasets and render in items container
    const paramFilters = pick(opts.params, ['organization', 'category', 'tag'])
    const attributeFilters = pick(opts.el.data(), ['organization', 'category'])
    const filters = createDatasetFilters(defaults(paramFilters, attributeFilters))
    const filteredDatasets = filter(opts.datasets, filters)
    this._render(elements, filteredDatasets)

    // Search datasets listener
    const searchFunction = this._createSearchFunction(filteredDatasets)
    const handleSearch = debounce((query) => {
      const results = searchFunction(query)
      this._render(elements, results)
    }, 150)
    elements.searchQuery.on('keyup', (e) => handleSearch(e.currentTarget.value))
  }

  _render (elements, datasets) {
    if (datasets.length === 0) {
      setContent(elements.datasetsItems, EMPTY_STATE_HTML)
    } else {
      setContent(elements.datasetsItems, datasets.map(TmplDatasetItem))
    }
    setContent(elements.datasetsCount, countLabel(datasets.length))
  }

  // Returns a function that can be used to search an array of datasets
  // The function returns the filtered array of datasets
  _createSearchFunction (datasets) {
    const fuse = new Fuse(datasets, {
      keys: [
        { name: 'title', weight: 0.4 },
        { name: 'tags', weight: 0.25 },
        { name: 'keywords', weight: 0.2 },
        { name: 'notes', weight: 0.1 },
        { name: 'resource_names', weight: 0.05 }
      ],
      threshold: 0.4,
      minMatchCharLength: 1,
      includeScore: false,
      shouldSort: true
    })
    return function (query) {
      if (!query || query.trim().length === 0) return datasets
      return fuse.search(query).map(function (result) {
        return datasets[result.refIndex]
      })
    }
  }
}
