class Team < ApplicationRecord
  has_many :costumers
  validates :name, presence: true
end
