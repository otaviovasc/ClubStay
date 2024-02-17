class Customer < ApplicationRecord
  belongs_to :team
  has_many :cards

  validates :name, presence: true
  validates :email, presence: true

  # validates :tempo_de_assinatura, presence: true, numericality: { only_integer: true }
  # validates :historico_de_presenca_nos_jogos, presence: true, numericality: { only_integer: true }
  # validates :historico_de_socio, presence: true, numericality: { only_integer: true }
  # validates :numero_de_desistencias_no_periodo, presence: true, numericality: { only_integer: true }
  # validates :historico_de_preco_nos_planos, presence: true, numericality: true
  # validates :tipo_de_plano, presence: true
  # validates :quantos_membros, presence: true, numericality: { only_integer: true }
  # validates :planos_com_ingresso_incluso, inclusion: { in: [true, false] }
  # validates :estado_civil, presence: true
  # validates :risco_de_churn, presence: true, numericality: { greater_than_or_equal_to: 0, less_than_or_equal_to: 1 }
  # validates :feedback_sobre_servicos, presence: true, numericality: { only_integer: true }
  # validates :frequencia_de_compra_de_produtos, presence: true, numericality: { only_integer: true }

  def self.filter_by_params(params)
    customers = self.all

    # Add your filtering logic based on the provided params
    # customers = customers.where(some_other_attribute: params[:someOtherParam]) if params[:someOtherParam].present?
    customers
  end
end
