import ecommerce.shipping  # entire module
from ecommerce.shipping import calc_shipping

# ecommerce is package
# shipping is the module
# calc_shipping is a specific function


# using line 1 where shipping is object of the package
ecommerce.shipping.calc_shipping()
# using line 2
calc_shipping()