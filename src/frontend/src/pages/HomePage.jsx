import { useGemini } from "../context/GeminiContext";
import SearchBox from "../components/SearchBox";

const HomePage = () => {
  //
  const gemini = useGemini();
  console.log(gemini);

  return (
    <div>
      <div>
        <SearchBox />
      </div>
    </div>
  );
};
export default HomePage;

// const ProductPage = () => {
//     const products = useProducts();
//     console.log(products);

//     return (
//         <div>
//             <div>
//                 {products.map((product) => (
//                     <p key={product.id}>{product.title}</p>
//                 ))}
//             </div>
//         </div>
//     );
// };
// export default ProductPage;
