def add_variable_to_context(request):
    if request.user.groups.filter(name='vendor').exists():
        vendor_status = True

    else:
        vendor_status = False

    return {
        'vendor_status': vendor_status
    }