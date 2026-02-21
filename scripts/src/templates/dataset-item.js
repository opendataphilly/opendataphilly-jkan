export default (data) => (
`<dataset>
  <div class="browse-cat"><a href="${data.url}">${data.title}</a></div>
  ${data.notes || ''}
</dataset>`
)
