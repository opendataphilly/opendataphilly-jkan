document.addEventListener('DOMContentLoaded', () => {
  // =====================================================================
  // 1. UTILITIES
  // =====================================================================
  
  const getRawEl = (el) => (el && el.jquery ? el[0] : el)

  function queryByHook (hook, container = document) {
    return getRawEl(container).querySelector(`[data-hook~="${hook}"]`)
  }

  function queryAllByHook (hook, container = document) {
    return Array.from(getRawEl(container).querySelectorAll(`[data-hook~="${hook}"]`))
  }

  function queryByComponent (component, container = document) {
    return getRawEl(container).querySelector(`[data-component~="${component}"]`)
  }

  function queryAllByComponent (component, container = document) {
    const parent = getRawEl(container)
    return Array.from(parent.querySelectorAll(`[data-component~="${component}"]`))
  }

  function setContent (container, content) {
    const element = getRawEl(container)
    if (!element) return
    
    element.innerHTML = ''
    
    if (Array.isArray(content)) {
      content.forEach(item => {
        if (typeof item === 'string') {
          element.insertAdjacentHTML('beforeend', item)
        } else {
          element.appendChild(item)
        }
      })
    } else {
      if (typeof content === 'string') {
        element.innerHTML = content
      } else if (content) {
        element.appendChild(content)
      }
    }
    return element
  }

  function slugify (text) {
    return text.toString().toLowerCase().trim()
      .replace(/[^ÆØÅæøåa-zA-Z0-9]/g, '-')  
      .replace(/\-\-+/g, '-')              
      .replace(/^\-|\-$/i, '')              
  }

  function createDatasetFilters (filters) {
    return function (dataset) {
      const conditions = []
      if (filters.organization) {
        conditions.push(dataset.organization && slugify(dataset.organization) === filters.organization)
      }
      if (filters.category) {
        const categories = Array.isArray(dataset.category) ? dataset.category : [dataset.category]
        conditions.push(categories.some(c => c && slugify(c) === filters.category))
      }
      return conditions.every(c => c)
    }
  }

  function collapseListGroup (container, show) {
    const element = getRawEl(container)
    if (!element) return

    if (!show) show = parseInt(element.dataset.show, 10) || 5

    const allItems = Array.from(element.querySelectorAll('.list-group-item'))
    const itemsToHide = allItems.filter((item, index) => index >= show && !item.classList.contains('active'))

    if (itemsToHide.length) {
      itemsToHide.forEach(item => item.style.display = 'none')

      const showMoreButton = document.createElement('a')
      showMoreButton.href = '#'
      showMoreButton.className = 'list-group-item list-group-item-action text-center text-primary fw-bold'
      showMoreButton.textContent = `Show ${itemsToHide.length} more...`

      showMoreButton.addEventListener('click', function (e) {
        itemsToHide.forEach(item => item.style.display = '')
        showMoreButton.remove()
        e.preventDefault()
      })
      element.appendChild(showMoreButton)
    }
  }

  function groupBy (array, prop) {
    return array.reduce((acc, item) => {
      const key = item[prop]
      if (!acc[key]) acc[key] = []
      acc[key].push(item)
      return acc
    }, {})
  }

  // =====================================================================
  // 2. TEMPLATES (Matching your Jekyll styles)
  // =====================================================================
  
  // Renders the list items on the sidebar (Categories and Organizations)
  function TmplListGroupItem (data) {
    const activeClass = data.selected ? 'active' : '';
    const badgeClass = data.selected ? 'bg-light text-dark' : 'bg-primary';
    
    return `<a href="${data.url}" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center ${activeClass}">
              ${data.title}
              <span class="badge rounded-pill ${badgeClass}">${data.count}</span>
            </a>`
  }

  // Renders individual datasets in the main search list
  function TmplDatasetItem (dataset) {
    // Falls back to baseurl path if available, or just standard dataset URL
    const baseUrl = (typeof settings !== 'undefined' && settings.BASE_URL) ? settings.BASE_URL : '';
    
    return `<dataset>
              <div class="browse-cat">
                <a href="${baseUrl}${dataset.url || '#'}">${dataset.title || 'Untitled'}</a>
              </div>
              <div>${dataset.notes || ''}</div>
            </dataset>`
  }

  // =====================================================================
  // 3. COMPONENTS
  // =====================================================================

  class DatasetFilter {
    constructor ({ el, datasets, params, type }) {
      const container = getRawEl(el)
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

      const mapped = Object.entries(bundled).map(([itemKey, datasetsInGroup]) => {
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
          url: '?' + new URLSearchParams(itemParams).toString(),
          count: filteredDatasets.length,
          unfilteredCount: datasetsInGroup.length,
          selected: selected
        }
      })

      return mapped.sort((a, b) => b.unfilteredCount - a.unfilteredCount)
    }
  }

  class DatasetsList {
    constructor ({ el, datasets, params }) {
      const container = getRawEl(el)

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
      const attributeFilters = extractFilters(container.dataset) 
      const combinedFilters = { ...attributeFilters, ...paramFilters }

      const filters = createDatasetFilters(combinedFilters)
      const filteredDatasets = datasets.filter(filters)
      const datasetsMarkup = filteredDatasets.map(TmplDatasetItem)
      
      setContent(elements.datasetsItems, datasetsMarkup)

      const datasetSuffix = filteredDatasets.length === 1 ? '' : 's'
      const datasetsCountMarkup = filteredDatasets.length + ' dataset' + datasetSuffix
      setContent(elements.datasetsCount, datasetsCountMarkup)

      const searchFunction = this._createSearchFunction(filteredDatasets)
      
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

  // =====================================================================
  // 4. INITIALIZATION
  // =====================================================================

  const urlSearchParams = new URLSearchParams(window.location.search)
  const params = Object.fromEntries(urlSearchParams.entries())

  let datasetsCache = null
  async function getDatasets () {
    if (!datasetsCache) {
      // Determines site baseurl dynamically if settings block isn't explicitly configured
      const baseUrl = (typeof settings !== 'undefined' && settings.BASE_URL) ? settings.BASE_URL : '';
      const response = await fetch(`${baseUrl}/datasets.json`)
      datasetsCache = await response.json()
    }
    return datasetsCache
  }

  const components = [
    { tag: 'datasets-list', class: DatasetsList, usesDatasets: true },
    { tag: 'categories-filter', class: DatasetFilter, type: 'category', usesDatasets: true },
    { tag: 'organizations-filter', class: DatasetFilter, type: 'organization', usesDatasets: true }
  ]

  async function init () {
    for (const component of components) {
      const els = queryAllByComponent(component.tag)
      
      if (els.length > 0) {
        if (component.usesDatasets) {
          const datasets = await getDatasets()
          els.forEach(el => {
            new component.class({ el, params, datasets, type: component.type })
          })
        }
      }
    }
  }

  init()
})
