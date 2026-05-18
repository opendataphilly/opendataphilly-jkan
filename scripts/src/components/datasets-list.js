import TmplDatasetItem from '../templates/dataset-item'
import { queryByHook, setContent, createDatasetFilters } from '../util'

export default class DatasetsList {
  constructor ({ el, datasets, params }) {
    const container = el.jquery ? el[0] : el

    const elements = {
      datasetsItems: queryByHook('datasets-items', container),
      datasetsCount: queryByHook('datasets-count', container),
      searchQuery: queryByHook('search-query', container)
    }

    const extractFilters = (source) => {
      const extracted = {}
      if (source && source.organization) extracted.organization = source.organization
      if (source && source.category) extracted.category = source.category
      return extracted
    }

    const paramFilters = extractFilters(params)
    // 1. Replaced el.data() with native container.dataset
    const attributeFilters = extractFilters(container.dataset) 
    const combinedFilters = { ...attributeFilters, ...paramFilters }

    const filters = createDatasetFilters(combinedFilters)
    const filteredDatasets = datasets.filter(filters)
    const datasetsMarkup = filteredDatasets.map(TmplDatasetItem)
    setContent(elements.datasetsItems, datasetsMarkup)

    const datasetSuffix = filteredDatasets.length > 1 ? 's' : ''
    const datasetsCountMarkup = filteredDatasets.length + ' dataset' + datasetSuffix
    setContent(elements.datasetsCount, datasetsCountMarkup)

    const searchFunction = this._createSearchFunction(filteredDatasets)
    
    // 2. Replaces elements.searchQuery.on('keyup') with addEventListener
    if (elements.searchQuery) {
      elements.searchQuery.addEventListener('keyup', (e) => {
        const query = e.currentTarget.value

        const results = searchFunction(query)
        const resultsMarkup = results.map(TmplDatasetItem)
        setContent(elements.datasetsItems, resultsMarkup)

        const resultsCountMarkup = results.length + ' datasets'
        setContent(elements.datasetsCount, resultsCountMarkup)
      })
    }
  }

  _createSearchFunction (datasets) {
    const keys = ['title', 'notes', 'tags', 'resource_names']
    return function (query) {
      const lowerCaseQuery = query.toLowerCase()
      return datasets.filter(function (dataset) {
        return keys.reduce(function (previousValue, key) {
          return previousValue || (dataset[key] && dataset[key].toLowerCase().includes(lowerCaseQuery))
        }, false)
      })
    }
  }
}
