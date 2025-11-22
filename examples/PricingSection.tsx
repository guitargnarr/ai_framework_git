// File: app/components/PricingSection.tsx

'use client'

import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Check } from 'lucide-react'

interface PricingTier {
  name: string
  description: string
  features: string[]
  price: string
}

const tiers: PricingTier[] = [
  {
    name: 'Basic',
    description: 'For small teams starting out.',
    features: ['10 users', '5GB storage', '24/7 support'],
    price: '$9.99/month'
  },
  {
    name: 'Pro',
    description: 'For growing teams.',
    features: ['Unlimited users', '20GB storage', 'Priority support'],
    price: '$19.99/month'
  },
  {
    name: 'Enterprise',
    description: 'For large organizations.',
    features: ['Custom solutions', 'Unlimited storage', '24/7 dedicated support'],
    price: '$49.99/month'
  }
]

export function PricingSection() {
  return (
    <div className="container mx-auto py-10">
      <h2 className="text-center text-3xl font-bold mb-8">Pricing</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {tiers.map((tier, index) => (
          <Card key={index} className={`shadow-lg ${tier.name === 'Pro' ? 'bg-gradient-to-r from-blue-500 to-purple-600 text-white' : ''}`}>
            <CardHeader>
              <CardTitle>{tier.name}</CardTitle>
              <CardDescription>{tier.description}</CardDescription>
            </CardHeader>
            <CardContent className="flex flex-col gap-4">
              {tier.features.map((feature, index) => (
                <div key={index} className="flex items-center space-x-2">
                  <Check size={16} />
                  <span>{feature}</span>
                </div>
              ))}
            </CardContent>
            <CardFooter className="flex justify-between items-center">
              <p className="text-xl font-bold">{tier.price}</p>
              <Button variant="default">Get Started</Button>
            </CardFooter>
          </Card>
        ))}
      </div>
    </div>
  )
}