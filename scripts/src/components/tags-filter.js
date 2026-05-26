import $ from 'jquery'
import {chain, pick, omit, filter, defaults} from 'lodash'

import TmplListGroupItem from '../templates/list-group-item'
import {setContent, slugify, createDatasetFilters, collapseListGroup} from '../util'

export default class {
  constructor (opts) {
    const tags = this._tagsWithCount(opts.datasets, opts.params)
    const tagsMarkup = tags.map(TmplListGroupItem)
    setContent(opts.el, tagsMarkup)
    collapseListGroup(opts.el)
  }

  _tagsWithCount (datasets, params) {
    return chain(datasets)
      .filter('tags')
      .flatMap(function (dataset) {
        if (!Array.isArray(dataset.tags) || dataset.tags.length === 0) return []
        // Emit one row per (dataset, tag) so we can group by tag below.
        return dataset.tags.map(function (tag) {
          return Object.assign({}, dataset, {_activeTag: tag})
        })
      })
      .groupBy('_activeTag')
      .map(function (datasetsForTag, tag) {
        const otherFilters = createDatasetFilters(pick(params, ['organization', 'category']))
        const filteredDatasets = filter(datasetsForTag, otherFilters)
        const tagSlug = slugify(tag)
        const selected = params.tag && params.tag === tagSlug
        const itemParams = selected ? omit(params, 'tag') : defaults({tag: tagSlug}, params)
        return {
          title: tag,
          url: '?' + $.param(itemParams),
          count: filteredDatasets.length,
          unfilteredCount: datasetsForTag.length,
          selected: selected
        }
      })
      .filter(function (item) { return item.count > 0 })
      .orderBy('unfilteredCount', 'desc')
      .value()
  }
}
