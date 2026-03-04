<h2>Models define the structure of core system entities.</h2>

<h3>They represent real-world objects in the domain.</h3>

<h3>Examples</h3>
<ul>
  <li>Restaurant</li>
  <li>Menu</li>
  <li>User</li>
  <li>Order</li>  
</ul>

<h3>These files contains the attributes not any logic</h3>

<p>
Example:

class Restaurant:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        </p>