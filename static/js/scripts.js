$(document).ready(function() {
    // SweetAlert confirmation for delete button
    $('.btn-danger').on('click', function(e) {
        e.preventDefault(); // Prevent form submission

        const deleteForm = $(this).closest('form'); // Get the form
        Swal.fire({
            title: 'Are you sure?',
            text: 'You will not be able to recover this meal!',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.isConfirmed) {
                // If confirmed, proceed with AJAX request for deletion
                $.ajax({
                    url: deleteForm.attr('action'), // URL from the form's action attribute
                    type: 'POST',
                    data: deleteForm.serialize(),
                    success: function(response) {
                        // Display success message using SweetAlert
                        Swal.fire({
                            title: 'Success!',
                            text: response.message,
                            icon: 'success'
                        }).then(() => {
                            // Optional: Redirect or perform any additional actions after confirmation
                            window.location.href = '/diet/meals/'; 
                        });
                    },
                    error: function(xhr, status, error) {
                        // Handle error if deletion fails
                        console.error(error);
                        // Show error message using SweetAlert if needed
                        Swal.fire({
                            title: 'Error!',
                            text: 'Failed to delete the meal',
                            icon: 'error'
                        });
                    }
                });
            }
        });
    });
});
