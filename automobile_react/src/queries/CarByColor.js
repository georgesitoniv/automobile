import gql from "graphql-tag";

export default gql`
  query CarByColor($colorId: ID){
    carByColor(colorId: $colorId) {
      id
      name
      order
      color{
        id
        name
      }
    }
  }
`;
