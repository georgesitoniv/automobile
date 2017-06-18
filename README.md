# automobile
Automobile website application. Developed using Django Web Framework as the back-end and React JS as the front-end.

The developer prepared two methods to view the project. The first method utilizes Django views and JQuery,it is accessible
at 'domain/django_views/'. It requires the Django local server to be running. The second method utilizes all of the Front End
technologies cited below, this method requires both the Django local server and the Express/Webpack-Dev server to be running.

Technology Used

  Back End:
    Django Web Framework,
    Graphene

  Front End:
    React JS,
    Redux,
    GraphQL,
    Apollo Client

Solution for the Constraints
  The developer added a slot number field for every Car Model. When the slot number of the selected Car Instance is increased,
  decreased, or changed, the selected Car Instance exchanges slot numbers with the Car Instance which has the desired
  slot number. This method limits the record updates into two queries.
  
