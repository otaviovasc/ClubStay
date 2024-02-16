class CreateCustomers < ActiveRecord::Migration[7.0]
  def change
    create_table :customers do |t|
      t.text :name
      t.references :team, null: false, foreign_key: true
      t.string :email
      t.integer :tempo_de_assinatura
      t.integer :historico_de_presenca_nos_jogos
      t.integer :historico_de_socio
      t.integer :numero_de_desistencias_no_periodo
      t.integer :historico_de_preco_nos_planos
      t.string :tipo_de_plano
      t.integer :quantos_membros
      t.string :planos_com_ingresso_incluso
      t.string :estado_civil
      t.string :risco_de_churn
      t.string :feedback_sobre_servicos
      t.string :frequencia_de_compra_de_produtos

      t.timestamps
    end
  end
end
