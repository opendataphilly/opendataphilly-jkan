import TmplListGroupItem from '../templates/list-group-item'
import { setContent, slugify, createDatasetFilters, collapseListGroup, groupBy } from '../util'

export default class DatasetFilter {
  constructor ({ el, datasets, params, type }) {
    const container = el.jquery ? el[0] : el
    this.type = type 
    this.crossType = this.type === 'category' ? 'organization' : 'category'

    const items = this._getItemsWithCount(datasets, params)
    const itemsMarkup = items.map(TmplListGroupItem)
    setContent(container, itemsMarkup)
    collapseListGroup(container)
  }

  _getItemsWithCount (datasets, params) {
    const type = this.type
    const crossType = this.crossType

    const exploded = datasets
      .filter(d => d && d[type])
      .flatMap(function (value) {
        if (!Array.isArray(value[type])) return value
        return value[type].map(function (item) {
          return { ...value, [type]: item }
        })
      })

    const bundled = groupBy(exploded, type)

    const mapped = Object.entries(bundled).map(function ([itemKey, datasetsInGroup]) {
      const pickedParams = params[crossType] ? { [crossType]: params[crossType] } : {}
      const filters = createDatasetFilters(pickedParams)
      const filteredDatasets = datasetsInGroup.filter(filters)
      
      const slug = slugify(itemKey)
      const selected = params[type] && params[type] === slug
      
      let itemParams
      if (selected) {
        const { [type]: _, ...rest } = params
        itemParams = rest
      } else {
        itemParams = { ...params, [type]: slug }
      }

      return {
        title: itemKey,
        // Replaced $.param() with native URLSearchParams configuration
        url: '?' + new URLSearchParams(itemParams).toString(),
        count: filteredDatasets.length,
        unfilteredCount: datasetsInGroup.length,
        selected: selected
      }
    })

    return mapped.sort((a, b) => b.unfilteredCount - a.unfilteredCount)
  }
}
