class AddAdditionalFieldsToCustomers < ActiveRecord::Migration[7.0]
  def change
    add_column :customers, :email, :string
    add_column :customers, :tempo_de_assinatura, :integer
    add_column :customers, :historico_de_presenca_nos_jogos, :integer
    add_column :customers, :historico_de_socio, :integer
    add_column :customers, :numero_de_desistencias_no_periodo, :integer
    add_column :customers, :historico_de_preco_nos_planos, :integer
    add_column :customers, :tipo_de_plano, :string
    add_column :customers, :quantos_membros, :integer
    add_column :customers, :planos_com_ingresso_incluso, :string
    add_column :customers, :estado_civil, :string
    add_column :customers, :risco_de_churn, :string
    add_column :customers, :feedback_sobre_servicos, :string
    add_column :customers, :frequencia_de_compra_de_produtos, :string
  end
end
