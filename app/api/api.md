<h2>The API layer defines HTTP endpoints.</h2>

<h3>Responsibilities:<h3>
<ul>
  <li>Define routes (GET, POST, PUT, DELETE)</li>
  <li>Accept request data</li>
  <li>Return responses</li>
  <li>Call the service layer</li>
</ul>

<h3>The API layer does NOT:</h3>
<li>Contain business logic</li>
<li>Access CSV files directly</li>

<h3>Example:</h3>
<p>
@router.get("/restaurants")
def get_restaurants():
    return restaurant_service.get_all()
    </p>