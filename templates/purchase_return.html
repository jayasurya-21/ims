<?php  include 'dashboard.php';?>
<?php  include 'links.php';?>



<?php

$host = "localhost";
$username = "root";
$password = "";
$database = "ims";
$purchase_invoice = '';
$show_form = true; // Flag variable to control form display

$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
<html>
<body>
<section id="content">
  
   <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        h2 {
            color: #333;
        }
      
        
        table {
            border-collapse: collapse;
            width: 100%;
        }
        table th, table td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        table th {
            background-color: #007bff;
            color: #fff;
        }
        input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            border: none;
            padding: 8px 16px;
            cursor: pointer;
            border-radius: 5px;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        input[type="number"],
        input[type="text"],
        input[type="checkbox"] {
            width: 100%;
            padding: 6px;
            margin: 4px 0;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
    </style>		

     <?php
if (isset($_POST['submit'])) {
    $show_form = false; // Set to false to hide the form after displaying details
   
    $purchase_invoice = $_POST['purchase_invoice'];

    $sql = "SELECT purchase.purchase_date, supplier.sup_name, product.product_id, product.product_name, product.category, product.brand, product.quantity
            FROM purchase
            INNER JOIN supplier ON purchase.sup_id = supplier.sup_id
            INNER JOIN product ON purchase.product_id = product.product_id
            WHERE purchase.purchase_invoice = '$purchase_invoice'";

    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $purchase_date = $row['purchase_date'];
        $supplier_name = $row['sup_name'];

        echo "<h2>Details for Purchase Invoice: $purchase_invoice</h2>";
        echo "<p><strong>Supplier Name:</strong> $supplier_name</p>";
        echo "<p><strong>Purchase Date:</strong> $purchase_date</p>";

        echo "<form method='post'>";
        echo "<input type='hidden' name='purchase_invoice' value='$purchase_invoice'>"; // Hidden input to retain value

        echo "<h3>Return Products:</h3>";
        echo "<table border='1'>
                <tr>
                    <th>Product Name</th>
                    <th>Category</th>
                    <th>Brand</th>
                    <th>Quantity Purchased</th>
                    <th>Return Quantity</th>
                    <th>Return Reason</th>
                    <th>Return?</th>
                </tr>";

        do {
            echo "<tr>
                    <td>{$row['product_name']}</td>
                    <td>{$row['category']}</td>
                    <td>{$row['brand']}</td>
                    <td>{$row['quantity']}</td>
                    <td><input type='number' name='return_quantity[]' value='0' min='0' max='{$row['quantity']}'></td>
                    <td><input type='text' name='return_reason[]'></td>
                    <td><input type='checkbox' name='return_product[]' value='true'></td>
                </tr>";
                echo "<input type='hidden' name='return_product[]' value=false>";
                echo "<input type='hidden' name='product_id[]' value='{$row['product_id']}'>";
        } while ($row = $result->fetch_assoc());

        echo "</table>";
        echo "<input type='submit' name='return_submit' value='Return Products'>";
        echo "</form>";
    } else {
        echo "No data found for Purchase Invoice: $purchase_invoice";
    }
}

if (isset($_POST['return_submit'])) {
    $return_products = $_POST['return_product'];
    $return_quantities = $_POST['return_quantity'];
    $return_reasons = $_POST['return_reason'];
    $purchase_invoice = $_POST['purchase_invoice']; 
    $productIds = $_POST['product_id'] ?? [];// Updated here to capture the purchase_invoice value
    echo "alert($purchase_invoice)";

    $stmt = $conn->prepare("INSERT INTO purchase_return (purchase_invoice, product_id, return_quantity, return_reason, return_date) 
                             VALUES (?, ?, ?, ?, ?)");

    $date = date('Y-m-d'); // Get current date

    if ($stmt) {
        $stmt->bind_param("siiss", $purchase_invoice, $product_id, $return_quantity, $return_reason, $date);

        foreach ($return_products as $index => $isChecked) {
            if ($isChecked === 'true') {
            $return_quantity = $return_quantities[$index];
            $return_reason = $return_reasons[$index];
            $productId = $productIds[$index];
            
            // Execute the prepared statement
            $stmt->execute();
             // Update product quantity
             $update_sql = "UPDATE product SET quantity = quantity - $return_quantity WHERE product_id = $product_id";
             $conn->query($update_sql);
        }

        echo 'alert("Products returned successfully!")';
        // You can redirect or display a success message here
    }
    }else{
        echo 'no data';
    }
    $stmt->close();
}
?>
 

            
      
</section> 
</html>


<!DOCTYPE html>
<html lang="en">

<head>
    <title>Purchase Return</title>
    <!-- Your head content here -->
</head>
<style>

h1.title {
    background-color: blue; /* Set h1 background color to blue */
    color: white; /* Set text color for h1 */
    padding: 10px;
}

ul.breadcrumbs {
    list-style: none;
    padding: 0;
    background-color: #f0f0f0; /* Set breadcrumbs background color */
    margin-top: 10px;
}

ul.breadcrumbs li {
    display: inline-block;
    padding: 5px;
}

ul.breadcrumbs li.divider {
    margin: 0 5px;
    color: #999;
}

ul.breadcrumbs li a {
    text-decoration: none;
    color: blue; /* Set link color for breadcrumbs */
}

ul.breadcrumbs li a.active {
    color: black; /* Set active link color */
    font-weight: bold;
}


        
</style>
<body>
    <section id ="content">
        
            <?php if ($show_form) { ?>
                <h1 class="title" style="margin-bottom: 10px;">PURCHASE RETURN</h1>
                        <ul class="breadcrumbs">
                            <li><a href="home.php">Home</a></li>
                            <li class="divider">/</li>
                            <li><a href="#" class="active">RETURN</a></li>
                        </ul>
            
                    <!-- Display the form only if $show_form is true -->
                    <form method="post">
                        <label for="purchase_invoice">Enter Purchase Invoice Number:</label>
                        <input type="text" name="purchase_invoice" id="purchase_invoice" required>
                        <input type="submit" name="submit" value="Submit">
                    </form>
                <?php } ?>

                </section>
         
            </body>
              

</html>
