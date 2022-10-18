from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode




def get_Tabls(data):   
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=False,
        # theme='blue', #Add theme color to the table
        enable_enterprise_modules=True,
        height=500, 
        width='100%',
        reload_data=True

    )
