

def get_data_by_name(data_variable_name):
    if data_variable_name == 'dassem':
        url_data = 'balanco_energia_dessem_tm/BALANCO_ENERGIA_DESSEM_'
        data_name = 'dassem'

    elif data_variable_name == 'ear_subsis_dia':
        url_data = 'ear_subsistema_di/EAR_DIARIO_SUBSISTEMA_'
        data_name = 'ear_subsis_dia'

    elif data_variable_name == 'balanco_energ_subs_ho':
        url_data = 'balanco_energia_subsistema_ho/BALANCO_ENERGIA_SUBSISTEMA_'
        data_name = 'balanco_energ_subs_ho'

    elif data_variable_name == 'capacidade-geracao':
        url_data = 'capacidade_geracao/CAPACIDADE_GERACAO_'
        data_name = 'capacidade_geracao'
    
    elif data_variable_name == 'capacidade-transformacao':
        url_data = 'capacidade_transformacao/CAPACIDADE_TRANSFORMACAO_'
        data_name = 'capacidade_transformacao'

    elif data_variable_name == 'cmo_se':
        url_data = 'cmo_se/CMO_SEMANAL_'
        data_name = 'cmo_se'
    
    elif data_variable_name == 'cmo_tm':
        url_data = 'cmo_tm/CMO_SEMIHORARIO_'
        data_name = 'cmo_tm'
    
    elif data_variable_name == 'curva_carga_ho':
        url_data = 'curva-carga-ho/CURVA_CARGA_'
        data_name = 'curva_carga_ho'
    
    elif data_variable_name == 'cvu_usitermica_se':
        url_data = 'cvu_usitermica_se/CVU_USINA_TERMICA_'
        data_name = 'cvu_usitermica_se'
    
    elif data_variable_name == 'ear_bacia_di':
        url_data = 'ear_bacia_di/EAR_DIARIO_BACIAS_'
        data_name = 'ear_bacia_di'
    
    elif data_variable_name == 'ear_ree_di':
        url_data = 'ear_ree_di/EAR_DIARIO_REE_'
        data_name = 'ear_ree_di'
    
    elif data_variable_name == 'ena_bacia_di':
        url_data = 'ena_bacia_di/ENA_DIARIO_BACIAS_'
        data_name = 'ena_bacia_di'
    
    elif data_variable_name == 'energia_vertida_turbinavel_ho':
        url_data = 'energia_vertida_turbinavel_ho/ENERGIA_VERTIDA_TURBINAVEL_'
        data_name = 'energia_vertida_turbinavel_ho'

    elif data_variable_name == 'quipamento_controle_reativo':
        url_data = 'quipamento_controle_reativo/EQP_CONTROLE_REATIVO_'
        data_name = 'equipamento_controle_reativo'

    elif data_variable_name == 'grandezas_fluviometricas_di':
        url_data = 'grandezas_fluviometricas_di/GRANDEZAS_FLUVIOMETRICAS_'
        data_name = 'grandezas_fluviometricas'

    elif data_variable_name == 'ind_disponibilidade_geracao_me':
        url_data = 'ind_disponibilidade_geracao_me/IND_DISPONIBILIDADE_GERACAO_'
        data_name = 'ind_disponibilidade_geracao_me'

    elif data_variable_name == 'ind_disponibilidade_ft_reativo_me':
        url_data = 'ind_disponibilidade_ft_reativo_me/IND_DISPONIBILIDADE_FT_REATIVO_'
        data_name = 'ind_disponibilidade_ft_reativo_me'

    elif data_variable_name == 'ind_disponibilidade_ft_conversor_me':
        url_data = 'ind_disponibilidade_ft_conversor_me/IND_DISPONIBILIDADE_FT_CONVERSOR_'
        data_name = 'ind_disponibilidade_ft_conversor_me'

    elif data_variable_name == 'ind_disponibilidade_ft_trlt_me':
        url_data = 'ind_disponibilidade_ft_trlt_me/IND_DISPONIBILIDADE_FT_TRLT_'
        data_name = 'ind_disponibilidade_ft_trlt_me'

    elif data_variable_name == 'intercambio_nacional_ho':
        url_data = 'intercambio_nacional_ho/INTERCAMBIO_NACIONAL_'
        data_name = 'intercambio_nacional'

    elif data_variable_name == 'intercambio_internacional_ho':
        url_data = 'intercambio_internacional_ho/INTERCAMBIO_INTERNACIONAL_'
        data_name = 'intercambio_internacional'

    elif data_variable_name == 'ofertapreco-importacao-se':
        url_data = 'ofertapreco-importacao-se/OFERTA_PRECO_IMPORTACAO_'
        data_name = 'ofertapreco_importacao'

    return url_data, data_name
