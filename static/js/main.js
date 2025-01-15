// Search functionality
document.addEventListener('DOMContentLoaded', function() {
  // Global search in dashboard
  const searchInput = document.querySelector('.search-bar input');
  if (searchInput) {
      searchInput.addEventListener('input', function(e) {
          const searchTerm = e.target.value.toLowerCase();
          
          // Search in recipes
          document.querySelectorAll('.recipe-circle').forEach(recipe => {
              const recipeName = recipe.querySelector('h5').textContent.toLowerCase();
              recipe.style.display = recipeName.includes(searchTerm) ? '' : 'none';
          });

          // Search in inventory (if on inventory page)
          document.querySelectorAll('tbody tr').forEach(row => {
              const productName = row.querySelector('td:first-child').textContent.toLowerCase();
              row.style.display = productName.includes(searchTerm) ? '' : 'none';
          });
      });
  }

  // Inventory category filtering
  const categoryFilters = document.querySelectorAll('.category-filter');
  categoryFilters.forEach(filter => {
      filter.addEventListener('change', function() {
          const category = this.value;
          const rows = document.querySelectorAll('tbody tr');
          
          rows.forEach(row => {
              if (category === 'all' || row.dataset.category === category) {
                  row.style.display = '';
              } else {
                  row.style.display = 'none';
              }
          });
      });
  });

  // Recipe modal image preview
  const imageInput = document.querySelector('input[type="file"]');
  if (imageInput) {
      imageInput.addEventListener('change', function() {
          if (this.files && this.files[0]) {
              const reader = new FileReader();
              reader.onload = function(e) {
                  const preview = document.querySelector('#image-preview');
                  if (preview) {
                      preview.src = e.target.result;
                      preview.style.display = 'block';
                  }
              };
              reader.readAsDataURL(this.files[0]);
          }
      });
  }
});

// Add to inventory functionality
function updateQuantity(itemId, change) {
  fetch(`/inventory/update/${itemId}/`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      },
      body: JSON.stringify({ change: change })
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          document.querySelector(`#quantity-${itemId}`).textContent = data.new_quantity;
      }
  });
}