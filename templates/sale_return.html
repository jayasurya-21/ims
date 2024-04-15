<?php  include 'dashboard.php';?>
<?php  include 'links.php';?>
<?php
$host = "localhost";
$username = "root";
$password = "";
$database = "ims";
$showForm = true;

$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

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
                    $showForm = false; // Hide the form after displaying details
                    $salesInvoiceId = $_POST['sales_invoice_id'];

                    $sql = "SELECT si.sales_date, c.cus_name, s.product_id, p.product_name, p.category, p.brand, s.quantity
                            FROM sales_invoice si
                            INNER JOIN customer c ON si.cus_id = c.cus_id
                            INNER JOIN sale s ON si.sales_invoice_id = s.sales_invoice_id
                            INNER JOIN product p ON s.product_id = p.product_id
                            WHERE si.sales_invoice_id = ?";

                    $stmt = $conn->prepare($sql);
                    $stmt->bind_param("s", $salesInvoiceId);
                    $stmt->execute();
                    $result = $stmt->get_result();

                    if ($result->num_rows > 0) {
                        $row = $result->fetch_assoc();
                        $salesDate = $row['sales_date'];
                        $customerName = $row['cus_name'];

                        echo "<h2>Details for Sales Invoice: $salesInvoiceId</h2>";
                        echo "<p><strong>Customer Name:</strong> $customerName</p>";
                        echo "<p><strong>Sales Date:</strong> $salesDate</p>";

                        echo "<form method='post'>";
                        echo "<input type='hidden' name='sales_invoice_id' value='$salesInvoiceId'>"; // Retain value

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
                                    <td><input type='text' name='return_reason[]' value=''></td>
                                    <td><input type='checkbox' name='return_product[]' value='true'></td>
                                </tr>";
                                echo "<input type='hidden' name='return_product[]' value=false>";
                                echo "<input type='hidden' name='product_id[]' value='{$row['product_id']}'>";
                        } while ($row = $result->fetch_assoc());

                        echo "</table>";
                        echo "<input type='submit' name='return_submit' value='Return Products'>";
                        echo "</form>";
                    } else {
                        echo "No data found for Sales Invoice: $salesInvoiceId";
                    }
                }

                // 


                if (isset($_POST['return_submit'])) {
                    $returnProducts = isset($_POST['return_product']) ? $_POST['return_product'] : [];
                    $returnQuantities = $_POST['return_quantity'] ?? [];
                    $returnReasons = $_POST['return_reason'] ?? [];
                    $salesInvoiceId = $_POST['sales_invoice_id'];
                    $productIds = $_POST['product_id'] ?? [];

                    $stmt = $conn->prepare("INSERT INTO sales_return (sale_id, product_id, returned_quantity, return_reason, return_date) 
                                            VALUES (?, ?, ?, ?, NOW())");

                    if ($stmt) {
                        $stmt->bind_param("siis", $salesInvoiceId, $productId, $returnQuantity, $returnReason);
                        foreach ($_POST['return_product'] as $index => $isChecked)
                        {
                            // Check if the product is marked for return
                            if ($isChecked === 'true') {
                                $productId = $productIds[$index];
                                $returnQuantity = $returnQuantities[$index];
                                $returnReason = $returnReasons[$index];
                                $isChecked=$returnProducts[$index];

                                echo "index: $index, product_id: $productId, return_quantity: $returnQuantity, return_reason: $returnReason,ischecked: $isChecked---------------";

                                // Your SQL queries to insert into sales_return and update product quantity
                                // ...

                                $stmt->execute();
                                $updateSql = "UPDATE product SET quantity = quantity + $returnQuantity WHERE product_id = $productId";
                                $conn->query($updateSql);

                                $updateSalesSql = "UPDATE sale SET return_status = 1 WHERE sales_invoice_id = $salesInvoiceId AND product_id = $productId";
                                $conn->query($updateSalesSql);

                                }else{
                                echo 'no data';
                            }
                            
                        }

                        echo '<script>alert("Products returned successfully!")</script>';
                    } else {
                        echo "Failed to prepare the statements.";
                    }

                    $stmt->close();
                } 
                ?>
 

            
      
</section>    
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
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
<section id="content">
   <main>
           <?php if ($showForm) { ?>
			<h1 class="title">SALES RETURN</h1>
			<ul class="breadcrumbs">
				<li><a href="home.php">Home</a></li>
				<li class="divider">/</li>
				<li><a href="#" class="active">RETURN</a></li>
			</ul>
            
            <h2>Return Products from Sales</h2>
            <form method="post">
                <label for="sales_invoice_id">Enter Sales Invoice Number:</label>
                <input type="text" name="sales_invoice_id" id="sales_invoice_id" required>
                <input type="submit" name="submit" value="Submit">
            </form>
            <?php } ?>


 

            
      </main>
</section>    
</body>
</html>
