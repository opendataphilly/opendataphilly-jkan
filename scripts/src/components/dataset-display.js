import { queryAllByHook, queryByHook } from '../util'

export default class DatasetDisplay {
  constructor ({ el }) {
    const container = el.jquery ? el[0] : el
    const resourceItems = queryAllByHook('resource-item', container)

    // 1. Replaced elements.resourceItem.each with native .forEach
    resourceItems.forEach((item) => {
      // 2. Replaced $('table tr', item) with native querySelector
      if (item.querySelector('table tr')) {
        const showDetailsBtn = queryByHook('show-resource-details', item)
        if (showDetailsBtn) showDetailsBtn.style.display = ''
      }
    })

    // 3. Replaced jQuery event delegation with a clean native event listener
    container.addEventListener('click', (e) => {
      const targetBtn = e.target.closest('[data-hook~=show-resource-details]')
      if (targetBtn) {
        const item = targetBtn.closest('[data-hook~=resource-item]')
        const details = item ? queryByHook('resource-details', item) : null
        
        if (details) {
          // Toggle visibility natively
          details.style.display = details.style.display === 'none' ? '' : 'none'
        }
        e.preventDefault()
      }
    })
  }
}
