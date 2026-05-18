// util.js

/**
 * Helper to safely extract a raw DOM element if a jQuery object 
 * is accidentally passed during migration.
 */
const getRawEl = (el) => (el && el.jquery ? el[0] : el)

export function queryByHook (hook, container = document) {
  return getRawEl(container).querySelector(`[data-hook~="${hook}"]`)
}

export function queryAllByHook (hook, container = document) {
  return Array.from(getRawEl(container).querySelectorAll(`[data-hook~="${hook}"]`))
}

export function queryByComponent (component, container = document) {
  return getRawEl(container).querySelector(`[data-component~="${component}"]`)
}

export function queryAllByComponent (component, container = document) {
  const parent = getRawEl(container)
  return Array.from(parent.querySelectorAll(`[data-component~="${component}"]`))
}

export function setContent (container, content) {
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

// Meant to mimic Jekyll's slugify function
// https://github.com/jekyll/jekyll/blob/master/lib/jekyll/utils.rb#L142
export function slugify (text) {
  return text.toString().toLowerCase().trim()
    .replace(/[^ÆØÅæøåa-zA-Z0-9]/g, '-')  // Replace non-alphanumeric chars with -
    .replace(/\-\-+/g, '-')              // Replace multiple - with single -
    .replace(/^\-|\-$/i, '')             // Remove leading/trailing hyphen
}

export function createDatasetFilters (filters) {
  return function (dataset) {
    const conditions = []
    if (filters.organization) {
      conditions.push(dataset.organization && slugify(dataset.organization) === filters.organization)
    }
    if (filters.category) {
      conditions.push(dataset.category && slugify(dataset.category).indexOf(filters.category) !== -1)
    }
    return conditions.every(function (value) { return !!value })
  }
}

// Collapses a bootstrap list-group to only show a few items by default
export function collapseListGroup (container, show) {
  const element = getRawEl(container)
  if (!element) return

  if (!show) show = parseInt(element.dataset.show, 10) || 5

  const allItems = Array.from(element.querySelectorAll('.list-group-item'))
  const itemsToHide = allItems.filter((item, index) => index >= show && !item.classList.contains('active'))

  if (itemsToHide.length) {
    itemsToHide.forEach(item => item.style.display = 'none')

    const showMoreButton = document.createElement('a')
    showMoreButton.href = '#'
    showMoreButton.className = 'list-group-item'
    showMoreButton.textContent = `Show ${itemsToHide.length} more...`

    showMoreButton.addEventListener('click', function (e) {
      itemsToHide.forEach(item => item.style.display = '')
      showMoreButton.remove()
      e.preventDefault()
    })
    element.appendChild(showMoreButton)
  }
}

// Native replacement for _.groupBy
export function groupBy (array, prop) {
  return array.reduce((acc, item) => {
    const key = item[prop]
    if (!acc[key]) acc[key] = []
    acc[key].push(item)
    return acc
  }, {})
}
