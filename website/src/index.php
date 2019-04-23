<html>
    <head>
        <title>Ejemplo</title>
    </head>

    <body>
        <h1>Inventario =)</h1>
        <ul>
            <?php

            $result = file_get_contents('http://product-service/');
            #echo "HOLAjjj......";
            $productos = json_decode($result,true);
            foreach($productos as $producto)
            {
                echo "<br>";
                echo "<li>";
                echo $producto["id"];
                echo "</li>";
                echo "<li>";
                echo $producto["nombre"];
                echo "</li>";
                

                
            }
            
            #$pro = json_decode($result,true)[0];
            #var_dump($pro["nombre"]);
            #$products = $obj->products;

            #foreach ($products as $product) {
            #   echo "<li>$product</li>";
            #}
            #echo $obj;
             
            ?>
        </ul>
    </body>
</html>
