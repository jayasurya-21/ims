<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Dynamic Invoice</title>
    <style>
        /* Your CSS styles here */
        .invoice-box {
            max-width: 800px;
            margin: auto;
            padding: 30px;
            border: 1px solid #eee;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
            font-size: 16px;
            line-height: 24px;
            font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
            color: #555;
        }

        /* Additional CSS for Print Button */
        .print-button {
            margin-top: 20px;
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* Table Styles */
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }
        @media print {
            .print-button {
                display: none;
            }
        }
    </style>
</head>
<body>
    <div class="invoice-box">
        <?php
        // Start the session to access session variables
        session_start();

        // Assuming you have the sales invoice number stored in the session
        if (isset($_SESSION['salesInvoiceId'])) {
            $salesInvoiceId = $_SESSION['salesInvoiceId'];

            // Database connection details
            $host = "localhost";
            $username = "root";
            $password = "";
            $database = "ims";

            // Create a connection to the database
            $conn = new mysqli($host, $username, $password, $database);

            // Check the connection
            if ($conn->connect_error) {
                die("Connection failed: " . $conn->connect_error);
            }

            // Fetch invoice details
            $sqlInvoice = "SELECT si.sales_invoice_id, si.sales_date, si.total_amount, si.discount,
                        c.cus_name, c.cus_add, c.cus_email, c.cus_mob
                        FROM sales_invoice si
                        INNER JOIN customer c ON si.cus_id = c.cus_id
                        WHERE si.sales_invoice_id = '$salesInvoiceId'";

            $resultInvoice = $conn->query($sqlInvoice);

            if ($resultInvoice->num_rows > 0) {
                $invoiceData = $resultInvoice->fetch_assoc();

                // Display invoice header information
                echo "<h2>Invoice Number: " . $invoiceData['sales_invoice_id'] . "</h2>";
                echo "<p>Date: " . $invoiceData['sales_date'] . "</p>";
                echo "<p>Customer Name: " . $invoiceData['cus_name'] . "</p>";
                echo "<p>Customer Address: " . $invoiceData['cus_add'] . "</p>";
                echo "<p>Email: " . $invoiceData['cus_email'] . "</p>";
                echo "<p>Contact: " . $invoiceData['cus_mob'] . "</p>";

                // Fetch sales details
                $sqlSales = "SELECT p.product_name, s.quantity, s.price
                            FROM sale s
                            INNER JOIN product p ON s.product_id = p.product_id
                            WHERE s.sales_invoice_id = '$salesInvoiceId'";

                $resultSales = $conn->query($sqlSales);

                if ($resultSales->num_rows > 0) {
                    // Display sales details table
                    echo "<table>
                            <tr>
                                <th>Product Name</th>
                                <th>Quantity</th>
                                <th>Price</th>
                            </tr>";
                    while ($salesData = $resultSales->fetch_assoc()) {
                        echo "<tr>
                                <td>" . $salesData['product_name'] . "</td>
                                <td>" . $salesData['quantity'] . "</td>
                                <td>" . $salesData['price'] . "</td>
                            </tr>";
                    }
                    echo "</table>";
                } else {
                    echo "No sales details found.";
                }

                // Calculate amount payable after reducing discount
                $totalAmount = $invoiceData['total_amount'];
                $discount = $invoiceData['discount'];
                $amountPayable = $totalAmount - $discount;

                // Display total amount payable
                echo "<p>Total Amount: " . $totalAmount . "</p>";
                echo "<p>Discount: " . $discount . "</p>";
                echo "<p>Amount Payable: " . $amountPayable . "</p>";

                // Close the database connection
                $conn->close();
            } else {
                echo "No invoice found for the provided ID.";
            }
        } else {
            echo "Sales invoice ID not found in session.";
        }
        ?>
        <button class="print-button" onclick="window.print()">Print Invoice</button>
    </div>
        <!-- Print button -->
        
    
</body>
</html>
