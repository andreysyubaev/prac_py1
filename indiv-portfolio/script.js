function filterPortfolio(category) {
    const items = document.querySelectorAll('.portfolio-item');
    items.forEach(item => {
      if (category === 'all' || item.getAttribute('data-category') === category) {
        item.style.display = 'inline-block';
      } else {
        item.style.display = 'none';
      }
    });
  }
  