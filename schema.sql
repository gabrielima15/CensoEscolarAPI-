CREATE TABLE IF NOT EXISTS instituicoes_ensino (
    id_instituicao SERIAL PRIMARY KEY,
    co_entidade INTEGER NOT NULL DEFAULT 0,
    no_entidade TEXT NOT NULL DEFAULT '',
    no_uf TEXT NOT NULL DEFAULT '',
    sg_uf TEXT NOT NULL DEFAULT '',
    co_uf INTEGER NOT NULL DEFAULT 0,
    no_municipio TEXT NOT NULL DEFAULT '',
    co_municipio INTEGER NOT NULL DEFAULT 0,
    nu_ano_censo INTEGER NOT NULL DEFAULT 0,
    qt_mat_bas INTEGER DEFAULT 0,
    qt_mat_inf INTEGER DEFAULT 0,
    qt_mat_fund INTEGER DEFAULT 0,
    qt_mat_med INTEGER DEFAULT 0,
    qt_mat_prof INTEGER DEFAULT 0,
    qt_mat_eja INTEGER DEFAULT 0,
    qt_mat_esp INTEGER DEFAULT 0,
    ativo INTEGER DEFAULT 1
);