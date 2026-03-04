# Repository Layer

<h3>Repositories handle data access.</h3>

<h3>Since this project uses CSV instead of a database, repositories:</h3>
<ul>
  <li>Read data from CSV</li>
  <li>Write updates to CSV</li>
  <li>Convert raw data into domain models</li>
</ul>
<h3>Example:</h3>
<p>
class RestaurantRepository:
    def get_all(self):
        return pd.read_csv("restaurants.csv")
</p>
<h3>Repositories do NOT contain business logic.</h3>